function add() {

	var list, itemText;
	list = document.getElementById("todolist");
	var item = document.createElement("li")
	itemText = document.getElementById("textfield").value;
	item.innerHTML = itemText;
	list.appendChild(item);
}