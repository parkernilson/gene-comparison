<script lang="typescript">
	import ContentColumn from './ui/ContentColumn.svelte';
</script>

<style>
	:global(body) {
		padding: 0;
		font-family: Montserrat, sans-serif;
	}
	:root {
		--card-border-radius: 42px;
		--master-side-margins: 32px;
	}
</style>

<svelte:head>
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,400;1,700&display=swap" rel="stylesheet">
</svelte:head>

<ContentColumn>
	<h1>Gene Sequence Comparisons</h1>
</ContentColumn>