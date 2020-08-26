export default class Shader
{
	constructor(display, vertSrc, fragSrc)
	{
		let gl = display.gl;
		
		let vert = gl.createShader(gl.VERTEX_SHADER);
		let frag = gl.createShader(gl.FRAGMENT_SHADER);
		let prog = gl.createProgram();
		
		gl.shaderSource(vert, "#version 300 es\nprecision mediump float;\n" + vertSrc);
		gl.shaderSource(frag, "#version 300 es\nprecision mediump float;\n" + fragSrc);
		
		gl.compileShader(vert);
		gl.compileShader(frag);
		gl.attachShader(prog, vert);
		gl.attachShader(prog, frag);
		gl.linkProgram(prog);
		
		console.log("compile vertex shader: ", gl.getShaderInfoLog(vert));
		console.log("compile fragment shader: ", gl.getShaderInfoLog(frag));
		console.log("link shader program: ", gl.getProgramInfoLog(prog));
		
		this.prog = prog;
		this.gl = gl;
	}
	
	use()
	{
		this.gl.useProgram(this.prog);
	}
	
	setIndices(buf)
	{
		let gl = this.gl;
		
		gl.bindBuffer(gl.ELEMENT_ARRAY_BUFFER, buf.buf);
	}
	
	setFloat(name, val)
	{
		let gl = this.gl;
		let prog = this.prog;
		let loca = gl.getUniformLocation(prog, name);
		
		gl.uniform1f(loca, val);
	}
	
	setVec2(name, v)
	{
		let gl = this.gl;
		let prog = this.prog;
		let loca = gl.getUniformLocation(prog, name);
		
		gl.uniform2fv(loca, v);
	}
	
	setMatrix(name, mat)
	{
		let gl = this.gl;
		let prog = this.prog;
		let loca = gl.getUniformLocation(prog, name);
		
		gl.uniformMatrix4fv(loca, false, mat);
	}
	
	setTexture(name, tex, unit)
	{
		let gl = this.gl;
		let prog = this.prog;
		let loca = gl.getUniformLocation(prog, name);
		
		gl.activeTexture(gl.TEXTURE0 + unit);
		gl.bindTexture(gl.TEXTURE_2D, tex.tex);
		gl.uniform1i(loca, unit);
	}
	
	setCamera(camera)
	{
		this.setMatrix("mat", camera.mat);
	}
	
	setAttrib(name, buf, size)
	{
		let gl = this.gl;
		let prog = this.prog;
		let loca = gl.getAttribLocation(prog, name);
		
		gl.enableVertexAttribArray(loca);
		gl.bindBuffer(gl.ARRAY_BUFFER, buf.buf);
		gl.vertexAttribPointer(loca, size, gl.FLOAT, false, 0, 0);
	}
}
