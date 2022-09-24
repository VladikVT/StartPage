let shadow = document.getElementById("shadow")

let searchText = document.getElementById("search-text")
let urlExample = "https://yandex.ru/search/?text="

let addFavSiteMenu = document.getElementById("add-fav-site-menu")
let AFSMtoggle = -1

function search() {
	if (searchText.value != "") {
    	open(urlExample + searchText.value)
	}
}

function addFavSite() {
	AFSMtoggle *= -1
	if (AFSMtoggle == 1) {
		addFavSiteMenu.style.display = "block"
		shadow.style.display = "block"
	} else if (AFSMtoggle == -1) {
		addFavSiteMenu.style.display = "none"
		shadow.style.display = "none"
	}
}