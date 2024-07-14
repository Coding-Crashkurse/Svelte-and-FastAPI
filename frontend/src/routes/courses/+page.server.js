/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
	const username = import.meta.env.VITE_AUTH_USERNAME;
	const password = import.meta.env.VITE_AUTH_PASSWORD;
	const apiBaseUrl = import.meta.env.VITE_API_BASE_URL;
	const credentials = Buffer.from(`${username}:${password}`).toString('base64');

	let response;
	try {
		response = await fetch('http://localhost:4000/get_youtube_entries', {
			headers: {
				Authorization: `Basic ${credentials}`
			}
		});
		const data = await response.json();
		console.log('Fetched data:', data);
		return { courses: data };
	} catch (err) {
		console.log(err);
		return { courses: [] };
	}
}
