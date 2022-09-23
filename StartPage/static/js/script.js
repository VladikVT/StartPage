let searchText = document.getElementById("search-text")
let searchButton = document.getElementById("search-button")

let urlExample = "https://yandex.ru/search/?text="

function search() {
	if (searchText.value != "") {
    	open(urlExample + searchText.value)
	}
}