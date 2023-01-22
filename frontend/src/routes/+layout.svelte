<script>
	import '../app.css';
</script>

<div class="nav-wrapper bg-base-100 bg-black text-white absolute w-full">
	<div class="max-w-screen-xl flex justify-between mx-auto">
		<div class="flex items-center justify-center">
			<a class="btn btn-ghost normal-case text-xl">Coding Crashkurse</a>
		</div>
		<div class="flex">
			<a href="/" class="group text-white hover:text-sky-600 transition duration-300 p-2 m-2 text-xl">
				Home
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a href="/youtube" class="group text-white hover:text-sky-600 transition duration-300 p-2 m-2 text-xl">
				YouTube
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a href="/udemy" class="group text-white hover:text-sky-600 transition duration-300 p-2 m-2 text-xl">
				Udemy
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a href="/about" class="group text-white hover:text-sky-600 transition duration-300 p-2 m-2 text-xl">
				About
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
		</div>
	</div>
</div>


<slot />
