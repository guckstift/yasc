export default class Buffer
{
	constructor(display, dynamic, index, data)
	{
		let gl = display.gl
		
		this.dynamic = dynamic;
		this.index = index;
		
		let buf = gl.createBuffer();
		
		this.buf = buf;
		this.gl = display.gl;
		
		if(data) {
			this.update(data);
		}
		
	}
	
	update(data)
	{
		let gl = this.gl;
		
		let bind = this.index ? gl.ELEMENT_ARRAY_BUFFER : gl.ARRAY_BUFFER;
		
		gl.bindBuffer(bind, this.buf);
		gl.bufferData(bind, data, this.dynamic ? gl.DYNAMIC_DRAW : gl.STATIC_DRAW);
	}
}
