/** @type {import('./$types').PageServerLoad} */
export async function load({ fetch }) {
	const username = 'user'; // Replace with your actual username
	const password = 'password'; // Replace with your actual password
	const credentials = Buffer.from(`${username}:${password}`).toString('base64');

	let response;
	try {
		response = await fetch('http://localhost:4000/get_udemy_entries', {
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
