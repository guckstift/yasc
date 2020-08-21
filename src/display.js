export default class Display
{
	constructor()
	{
		this.frame = this.frame.bind(this);
		
		let canvas = document.createElement("canvas");
		let gl = canvas.getContext("webgl2", {antialias: false, alpha: false});
		
		document.body.appendChild(canvas);
		
		canvas.style.position = "absolute";
		canvas.style.left = "0";
		canvas.style.top = "0";
		canvas.style.width = "100%";
		canvas.style.height = "100%";
		
		this.canvas = canvas;
		this.gl = gl;
		
		requestAnimationFrame(this.frame);
		
		this.framecb = () => {};
	}
	
	getAspect()
	{
		return this.canvas.width / this.canvas.height;
	}
	
	get width()
	{
		return this.canvas.width;
	}
	get height()
	{
		return this.canvas.height;
	}
	
	frame()
	{
		let gl = this.gl;
		
		requestAnimationFrame(this.frame);
		
		let w = this.canvas.clientWidth;
		let h = this.canvas.clientHeight;
		
		if(w !== this.canvas.width || h !== this.canvas.height) {
			this.canvas.width = w;
			this.canvas.height = h;
			gl.viewport(0, 0, w, h);
		}
		
		this.framecb();
	}
	
	trianglestrip(count, indexed = false)
	{
		let gl = this.gl;
		
		if(indexed) {
			gl.drawElements(gl.TRIANGLE_STRIP, count, gl.UNSIGNED_INT, 0);
		}
		else {
			gl.drawArrays(gl.TRIANGLE_STRIP, 0, count);
		}
	}
}
