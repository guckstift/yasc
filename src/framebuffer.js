export default class Framebuffer
{
	constructor(display)
	{
		let gl = this.gl = display.gl;
		
		this.framebuf = gl.createFramebuffer();
		this.colortex = gl.createTexture();
		this.depthbuf = gl.createRenderbuffer();
		this.w = this.h = 0;
		
		gl.bindFramebuffer(gl.FRAMEBUFFER, this.framebuf);
		gl.bindTexture(gl.TEXTURE_2D, this.colortex);
		gl.bindRenderbuffer(gl.RENDERBUFFER, this.depthbuf);
		gl.framebufferTexture2D(gl.FRAMEBUFFER, gl.COLOR_ATTACHMENT0, gl.TEXTURE_2D, this.colortex, 0);
		gl.framebufferRenderbuffer(gl.FRAMEBUFFER, gl.DEPTH_ATTACHMENT, gl.RENDERBUFFER, this.depthbuf);
		gl.bindFramebuffer(gl.FRAMEBUFFER, null);
		
		this.display = display;
	}
	
	update()
	{
		let gl = this.gl;
		let display = this.display;
		
		if(this.w !== display.width || this.h !== display.height) {
			this.w = display.width;
			this.h = display.height;
			gl.bindTexture(gl.TEXTURE_2D, this.colortex);
			gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, this.w, this.h, 0, gl.RGBA, gl.UNSIGNED_BYTE, null);
			gl.bindRenderbuffer(gl.RENDERBUFFER, this.depthbuf);
			gl.renderbufferStorage(gl.RENDERBUFFER, gl.DEPTH_COMPONENT16, this.w, this.h);
		}
	}
	
	bind()
	{
		let gl = this.gl;
		
		gl.bindFramebuffer(gl.FRAMEBUFFER, this.framebuf);
		gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);
	}
	
	unbind()
	{
		let gl = this.gl;
		
		gl.bindFramebuffer(gl.FRAMEBUFFER, null);
	}
	
	getPixel(x, y)
	{
		let gl = this.gl;
		let pickbuf = new Uint8Array(4);
		
		gl.readPixels(x, this.h - y, 1, 1, gl.RGBA, gl.UNSIGNED_BYTE, pickbuf);
		
		return pickbuf;
	}
}
