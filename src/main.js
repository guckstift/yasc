import Display from "./display.js";
import Map from "./map.js";
import Camera from "./camera.js";

let display = new Display();
let map = new Map(display, 4);
let camera = new Camera(display);

display.framecb = function ()
{
	camera.update();
	map.draw(camera);
}
