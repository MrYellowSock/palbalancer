let allRows = Array.from(document.querySelectorAll("tr"));

let allRowsTD = allRows.map(row => Array.from(row.children))

let texts = allRowsTD.map(row => {
	return row.map(cell => {
		let img = cell.querySelector("img")
		if (img) {
			return img.src
		}
		return cell.innerText
	})
})
console.log( texts.map(row => row.join(",")).join("\n") )
