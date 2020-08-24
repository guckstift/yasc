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
