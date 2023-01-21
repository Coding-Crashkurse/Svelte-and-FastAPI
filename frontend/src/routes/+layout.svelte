<script>
	import '../app.css';
</script>

<div class="navbar bg-base-100 bg-black text-white">
	<div class="flex-1">
		<a class="btn btn-ghost normal-case text-xl">Coding Crashkurse</a>
	</div>
	<div>
		<a href="#" class="group text-sky-600 transition duration-300 p-2 m-2 text-xl">
			Home
			<span
				class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
			/>
		</a>
		<a href="#" class="group text-sky-600 transition duration-300 p-2 m-2 text-xl">
			Home
			<span
				class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
			/>
		</a>
		<a href="#" class="group text-sky-600 transition duration-300 p-2 m-2 text-xl">
			Home
			<span
				class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
			/>
		</a>
		<a href="#" class="group text-sky-600 transition duration-300 p-2 m-2 text-xl">
			Home
			<span
				class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
			/>
		</a>
	</div>
	<div class="flex-none">
		<button class="btn btn-square btn-ghost">
			<svg
				xmlns="http://www.w3.org/2000/svg"
				fill="none"
				viewBox="0 0 24 24"
				class="inline-block w-5 h-5 stroke-current"
				><path
					stroke-linecap="round"
					stroke-linejoin="round"
					stroke-width="2"
					d="M4 6h16M4 12h16M4 18h16"
				/></svg
			>
		</button>
	</div>
</div>

<slot />
