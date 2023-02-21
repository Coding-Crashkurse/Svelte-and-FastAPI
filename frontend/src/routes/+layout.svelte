<script>
	import '../app.css';
	let year = new Date().getFullYear();
</script>

<div class="nav-wrapper bg-black p-2 text-white absolute w-full">
	<div class="max-w-screen-xl flex  justify-between mx-auto flex-col md:flex-row">
		<div class="flex items-center justify-center">
			<div class="btn btn-ghost normal-case text-xl">Coding Crashkurse</div>
		</div>

		<div class="flex justify-center">
			<a
				href="/"
				class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl"
			>
				Home
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a
				href="/kurse"
				class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl "
			>
				Kurse
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a
				href="/premium"
				class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl"
			>
				Premium
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a
				href="/about"
				class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl"
			>
				About
				<span
					class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
				/>
			</a>
			<a
			href="/kontakt"
			class="group text-white hover:text-sky-600 transition duration-300 p-2 md:m-2 md:text-xl"
		>
			Kontakt
			<span
				class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-sky-600"
			/>
		</a>
		</div>
	</div>
</div>

<slot />

<footer>
	<div class="footer bg-black h-10 text-white flex items-center">
		<div class="inline text-center w-full ">
			Copyright {year} Coding Crashkurse, All rights reserved | <a href="/impressum">Impressum</a> |
			<a href="/datenschutzerklaerung">Datenschutzerklärung</a>
		</div>
	</div>
</footer>
