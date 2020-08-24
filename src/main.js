import Display from "./display.js";
import Map from "./map.js";
import Camera from "./camera.js";

let display = new Display();
let map = new Map(display, 2);
let camera = new Camera(display);

map.setHeight(2, 2, 1);

display.framecb = function ()
{
	camera.update();
	map.draw(camera);
}
