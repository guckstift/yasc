export default class Display
{
	constructor()
	{
		this.onframe = this.onframe.bind(this);
		
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
		
		gl.enable(gl.DEPTH_TEST);
		
		requestAnimationFrame(this.onframe);
		
		this.frame = () => {};
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
	
	onframe()
	{
		let gl = this.gl;
		
		requestAnimationFrame(this.onframe);
		
		let w = this.canvas.clientWidth;
		let h = this.canvas.clientHeight;
		
		if(w !== this.canvas.width || h !== this.canvas.height) {
			this.canvas.width = w;
			this.canvas.height = h;
			gl.viewport(0, 0, w, h);
		}
		
		this.frame();
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
