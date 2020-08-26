import * as mat4 from "./glmatrix/mat4.js";
import * as glm from "./glmatrix/common.js";
import * as vec3 from "./glmatrix/vec3.js";

const viewAngle = Math.acos(1 / Math.sqrt(3));
const triaWidth = 64;

export default class Camera
{
	constructor(display)
	{
		this.display = display;
		this.mat = mat4.create();
		this.pos = vec3.create();
		this.scale = 64;
	}
	
	update()
	{
		let display = this.display;
		mat4.identity(this.mat);
		mat4.scale(this.mat, this.mat, [this.scale * 2 / display.width, this.scale * 2 / display.height, -1/256]);
		//mat4.perspective(this.mat, glm.toRadian(90), this.display.getAspect(), 0.1, 1000.0);
		mat4.translate(this.mat, this.mat, [0, 0, 4-4]);
		mat4.rotateX(this.mat, this.mat, -viewAngle);
		//mat4.rotateX(this.mat, this.mat, -Math.PI / 4);
		mat4.translate(this.mat, this.mat, this.pos);
		//mat4.rotateX(this.mat, this.mat, glm.toRadian(-50));
	}
}
