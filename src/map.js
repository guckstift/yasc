import Buffer from "./buffer.js";
import Shader from "./shader.js";
import Texture from "./texture.js";
import Framebuffer from "./framebuffer.js";

let vertSrc = picker => `
	uniform float mapsize;
	uniform mat4 mat;
	uniform sampler2D maptex;
	
	` + (picker ? `
		out vec3 distinction;
		out vec2 coord;
	` : `
		uniform vec2 pickedCoord;
		out vec2 uv;
		out float coef;
		out vec3 norm;
	`) + `
	
	vec3 getDistinctionColor(ivec2 mapcoord)
	{
		vec2 fmapcoord = vec2(mapcoord);
		
		return vec3(
			float(mod(fmapcoord.x - fmapcoord.y, 3.0) == 0.0),
			float(mod(fmapcoord.x - fmapcoord.y, 3.0) == 1.0),
			float(mod(fmapcoord.x - fmapcoord.y, 3.0) == 2.0)
		);
	}
	
	ivec2 getMapCoord(int vertId, float mapsize)
	{
		return ivec2(
			mod(float(vertId), mapsize),
			floor(float(vertId) / mapsize)
		);
	}
	
	vec3 getVertPos(sampler2D maptex, ivec2 mapcoord)
	{
		const float triaHeight = sqrt(3.0) / 2.0;
		vec2 fmapcoord = vec2(mapcoord);
		
		vec2 groundpos = vec2(
			fmapcoord.x + fmapcoord.y * 0.5,
			fmapcoord.y * triaHeight
		);
		
		vec4 texel = texelFetch(maptex, mapcoord, 0) * 255.0;
		float height = texel.r / 2.0;
		
		return vec3(groundpos, height);
	}
	
	vec3 getNormal(sampler2D maptex, ivec2 mapcoord)
	{
		vec3 v  = getVertPos(maptex, mapcoord);
		vec3 r  = getVertPos(maptex, mapcoord + ivec2(+1, 0)) - v;
		vec3 ru = getVertPos(maptex, mapcoord + ivec2( 0,+1)) - v;
		vec3 lu = getVertPos(maptex, mapcoord + ivec2(-1,+1)) - v;
		vec3 l  = getVertPos(maptex, mapcoord + ivec2(-1, 0)) - v;
		vec3 ld = getVertPos(maptex, mapcoord + ivec2( 0,-1)) - v;
		vec3 rd = getVertPos(maptex, mapcoord + ivec2(+1,-1)) - v;
		
		return normalize(
			cross(r, ru) + cross(ru, lu) + cross(lu, l) + cross(l, ld) + cross(ld, rd) + cross(rd, r)
		);
	}
	
	void main()
	{
		ivec2 mapcoord = getMapCoord(gl_VertexID, mapsize);
		vec3 vertpos = getVertPos(maptex, mapcoord);
		
		gl_Position = mat * vec4(vertpos, 1);
		
		` + (picker ? `
			distinction = getDistinctionColor(mapcoord);
			coord = vec2(mapcoord);
		` : `
			const vec3 sun = normalize(vec3(-1,-1,+1));
			vec3 normal = getNormal(maptex, mapcoord);
			
			coef = dot(sun, normal) * 4.0 - 1.5;
			//coef = clamp(dot(normal, sun) * 3.0 - 1.0, 0.0, 1.0);
			//coef = clamp(dot(normal, sun), 0.0, 1.0);
			norm = normal;
			uv = vertpos.xy;
			
			if(pickedCoord == vec2(mapcoord)) {
				coef += 2.0;
			}
		`) + `
	}
`;

let fragSrc = picker => `
	` + (picker ? `
		in vec3 distinction;
		in vec2 coord;
	` : `
		uniform sampler2D tex;
		in vec2 uv;
		in float coef;
	`) + `
	
	out vec4 color;
	
	vec2 pickCoord(vec2 coord, vec3 distinction)
	{
		float maxcol = max(distinction.r, max(distinction.g, distinction.b));
		float colid = maxcol == distinction.r ? 0.0 : maxcol == distinction.g ? 1.0 : 2.0;
		vec2 icoord = floor(coord);
		float pin = mod(colid - icoord.x + icoord.y, 3.0);
		float upper = floor(fract(coord.x) + fract(coord.y));
		
		return icoord + vec2(pin == 1.0, pin == 2.0) + vec2(pin == 0.0) * upper;
	}
	
	void main()
	{
		` + (picker ? `
			color = vec4(pickCoord(coord, distinction) / 256.0, 0, 1);
		` : `
			color = texture(tex, uv / 4.0, 0.0);
			color.rgb *= coef;
		`) + `
	}
`;

export default class Map
{
	constructor(display, size)
	{
		this.size = size;
		this.indexbuf = new Buffer(display, false, true);
		
		let indices = [];
		
		for(let y = 0, i = 0; y < size - 1; y++) {
			indices.push(i);
			
			for(let x = 0; x < size; x++, i++) {
				indices.push(i);
				indices.push(i + size);
			}
			
			indices.push(i + size - 1);
		}
		
		this.indexbuf.update(new Uint32Array(indices));
		this.display = display;
		this.shader = new Shader(display, vertSrc(false), fragSrc(false));
		this.pickshader = new Shader(display, vertSrc(true), fragSrc(true));
		this.vertcount = indices.length;
		this.tex = new Texture(display, "gfx/grass2.png");
		this.maptex = new Texture(display, null, size, size);
		this.data = new Uint8Array(size * size * 4);
		this.pickbuf = new Framebuffer(display);
	}
	
	setHeight(x, y, h)
	{
		this.data[4 * (x + y * this.size)] = h;
		this.maptex.update(this.data);
	}
	
	draw(camera, pickedCoord = [-1,-1])
	{
		let shader = this.shader;
		let display = this.display;
		
		shader.use();
		shader.setTexture("tex", this.tex, 0);
		shader.setTexture("maptex", this.maptex, 1);
		shader.setIndices(this.indexbuf);
		shader.setFloat("mapsize", this.size);
		shader.setVec2("pickedCoord", pickedCoord);
		shader.setCamera(camera);
		display.trianglestrip(this.vertcount, true);
	}
	
	pick(camera, x, y)
	{
		let shader = this.pickshader;
		let display = this.display;
		
		this.pickbuf.update();
		this.pickbuf.bind();
		
		shader.use();
		shader.setTexture("maptex", this.maptex, 1);
		shader.setIndices(this.indexbuf);
		shader.setFloat("mapsize", this.size);
		shader.setCamera(camera);
		display.trianglestrip(this.vertcount, true);
		
		let pixel = this.pickbuf.getPixel(x, y);
		
		this.pickbuf.unbind();
		
		if(pixel[3] > 0) {
			return [pixel[0], pixel[1]];
		}
	}
}
