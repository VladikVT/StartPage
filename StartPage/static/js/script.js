let shadowAFS = document.getElementById("shadow-afs")
let shadowANS = document.getElementById("shadow-ans")
let shadowS = document.getElementById("shadow-s")

let searchText = document.getElementById("search-text")
let urlExample = "https://yandex.ru/search/?text="

let addFavSiteMenu = document.querySelector("#add-fav-sites-menu")
let AFSMtoggle = -1

let addNewsSiteMenu = document.querySelector("#add-news-sites-menu")
let ANSMtoggle = -1

let SettingsMenu = document.querySelector("#settings-menu")
let SMtoggle = -1

function search() {
	if (searchText.value != "") {
    	open(urlExample + searchText.value)
	}
}

function addFavSite() {
	AFSMtoggle *= -1
	if (AFSMtoggle == 1) {
		addFavSiteMenu.style.display = "block"
		shadowAFS.style.display = "block"
	} else if (AFSMtoggle == -1) {
		addFavSiteMenu.style.display = "none"
		shadowAFS.style.display = "none"
	}
}

function addNewsSite() {
	ANSMtoggle *= -1
	if (ANSMtoggle == 1) {
		addNewsSiteMenu.style.display = "block"
		shadowANS.style.display = "block"
	} else if (ANSMtoggle == -1) {
		addNewsSiteMenu.style.display = "none"
		shadowANS.style.display = "none"
	}
}

function viewSettings() {
	SMtoggle *= -1
	if (SMtoggle == 1) {
		SettingsMenu.style.display = "block"
		shadowS.style.display = "block"
	} else if (SMtoggle == -1) {
		SettingsMenu.style.display = "none"
		shadowS.style.display = "none"
	}
}