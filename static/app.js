const arr = document.getElementsByClassName('options')

const editProduct = (id) => {
	javascript.history(`/edit?id=${id}`)
}


const handleClick = (event) => {
	const targetEl = event.target.classList[0]
	console.log(targetEl)
	if (targetEl === 'btn-modal') {
		event.target.parentElement.children[1].classList.toggle('active-modal')
	}

	if (targetEl === 'edit' || targetEl === 'buy') {
		const id = event.target.parentElement.getAttribute("data-id")
		console.log(id)

		switch (targetEl) {
			case 'edit':
				// editProduct(id)
				console.log('editing')
				break;
			case 'buy':
				// buyProduct(id)
				console.log('buying')
				break;
			default:
				// statements_def
				break;
		}
	}
}

for(var i = 0, length1 = arr.length; i < length1; i++){
	arr[i].addEventListener('click', handleClick)
}

