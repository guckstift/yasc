import Buffer from "./buffer.js";
import Shader from "./shader.js";

let vertSrc = `
	uniform float mapsize;
	uniform mat4 mat;
	out vec2 uv;
	
	void main()
	{
		const float triaHeight = sqrt(3.0) / 2.0;
		
		vec2 coord = vec2(
			mod(float(gl_VertexID), mapsize),
			floor(float(gl_VertexID) / mapsize)
		);
		
		vec2 groundpos = vec2(
			coord.x + coord.y * 0.5,
			coord.y * triaHeight
		);
		
		gl_Position = mat * vec4(groundpos, 0, 1);
		
		uv = groundpos;
	}
`;

let fragSrc = `
	in vec2 uv;
	out vec4 color;
	
	float random(vec2 uv)
	{
		uint x = uint(uv.x * 15485863.0);
		uint y = uint(uv.y * 285058399.0);
		
		if(x == 0u || y == 0u) {
			x += x ^ y;
		}
		else {
			x ^= x + y;
		}
		
		x ^= x >> 2;   // xor with r-shift with 1. prime
		x ^= x << 5;   // xor with l-shift with 3. prime
		x ^= x >> 11;  // xor with r-shift with 5. prime
		x ^= x << 17;  // xor with l-shift with 7. prime
		x ^= x >> 23;  // xor with r-shift with 9. prime
		x ^= x << 31;  // xor with l-shift with 11. prime
		
		return float(x) / float(0xffFFffFFu);
	}

	void main()
	{
		color = vec4(vec3(random(uv)),1);
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
		this.shader = new Shader(display, vertSrc, fragSrc);
		this.vertcount = indices.length;
	}
	
	draw(camera)
	{
		let shader = this.shader;
		let display = this.display;
		
		shader.use();
		shader.setIndices(this.indexbuf);
		shader.setFloat("mapsize", this.size);
		shader.setCamera(camera);
		display.trianglestrip(this.vertcount, true);
	}
}
