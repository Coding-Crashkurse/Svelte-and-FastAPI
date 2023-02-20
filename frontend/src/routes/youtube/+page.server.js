// eslint-disable-next-line @typescript-eslint/ban-ts-comment
// @ts-ignore
export async function load({ fetch }) {
	let response;
	try {
		response = await fetch('http://api:5000/get_entries');
	} catch (err) {
		console.log(err);
	}
	return await response.json();
}
