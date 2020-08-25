const MOUSE_BUTTONS = ["left", "middle", "right"];
const NOOP = () => {};

export default class Mouse
{
	constructor(display)
	{
		this.ondown = this.ondown.bind(this);
		this.onup = this.onup.bind(this);
		this.onmove = this.onmove.bind(this);
		this.onwheel = this.onwheel.bind(this);
		this.oncontextmenu = this.oncontextmenu.bind(this);
		this.onpointerlockchange = this.onpointerlockchange.bind(this);
		this.canvas = display.canvas;
		this.pos = [-1, -1];
		this.rel = [0, 0];
		this.locked = false;
		
		this.canvas.addEventListener("mousedown", this.ondown);
		this.canvas.addEventListener("mouseup", this.onup);
		this.canvas.addEventListener("mousemove", this.onmove);
		this.canvas.addEventListener("wheel", this.onwheel);
		this.canvas.addEventListener("contextmenu", this.oncontextmenu);
		document.addEventListener("pointerlockchange", this.onpointerlockchange);
		
		this.resetStates();
	}
	
	resetStates()
	{
		this.move = NOOP;
		this.down = {left: NOOP, right: NOOP, middle: NOOP, any: NOOP};
		this.up = {left: NOOP, right: NOOP, middle: NOOP, any: NOOP};
		this.wheel = {up: NOOP, down: NOOP, any: NOOP};
		this.buttons = {left: false, right: false, middle: false};
		this.pos = [0, 0];
		this.rel = [0, 0];
	}
	
	updateState(e)
	{
		let rect = this.canvas.getBoundingClientRect();
		this.pos[0] = e.clientX - rect.left;
		this.pos[1] = e.clientY - rect.top;
		this.rel[0] = e.movementX;
		this.rel[1] = e.movementY;
	}
	
	lock()
	{
		this.canvas.requestPointerLock();
	}
	
	unlock()
	{
		document.exitPointerLock();
	}
	
	ondown(e)
	{
		this.updateState(e);
		this.buttons[MOUSE_BUTTONS[e.button]] = true;
		this.down[MOUSE_BUTTONS[e.button]](e);
		this.down.any(e);
	}
	
	onup(e)
	{
		this.updateState(e);
		this.buttons[MOUSE_BUTTONS[e.button]] = false;
		this.up[MOUSE_BUTTONS[e.button]](e);
		this.up.any(e);
	}
	
	onmove(e)
	{
		this.updateState(e);
		this.move(e);
	}
	
	onwheel(e)
	{
		this.updateState(e);
		
		if(e.deltaY > 0) {
			this.wheel.down(e);
		}
		else {
			this.wheel.up(e);
		}
		
		this.wheel.any(e);
	}
	
	oncontextmenu(e)
	{
		e.preventDefault();
	}
	
	onpointerlockchange(e)
	{
		if(document.pointerLockElement === this.canvas) {
			this.locked = true;
		}
		else {
			this.locked = false;
		}
	}
}
