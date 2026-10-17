class APIClient {
    constructor(baseURL = '/api') {
        this.baseURL = baseURL;
    }

    async deleteItem(itemId) {
        const response = await fetch(`${this.baseURL}/items/${itemId}`, {method: 'DELETE'});
        return await response.json();
    }

    async fetchAllItems() {
        const response = await fetch(`${this.baseURL}/get-items`);
        return await response.json();
    }

    async addItem(itemData) {
        const response = await fetch(`${this.baseURL}/add-item`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(itemData)
        });
        return await response.json();
    }
}

class ItemCard {
    constructor(data) {
        this.data = data;
    }

    render() {
        `<div class="card-item" id="item">
            <div class="card-name">${this.data.name}</div>
            <div class="card-meta">
                <span><strong>Stock:</strong> ${this.data.quantity}</span>
                <span><strong>Owner:</strong> ${this.data.owner}</span>
                <span><strong>Valuation:</strong> ${this.data.valuation}</span>
                                
                <button class="delete-btn" onclick="Deletethis('${this.data.id}')">Delete</button>
            </div>
        </div>`
    }
}

const api = new APIClient()

async function Loadpage() {
    const itemlist = document.getElementById('item-list');
    itemlist.innerHTML = '';

    try {
        const items = await api.fetchAllItems();

        items.forEach(item => {
            const kard = new ItemCard(item);
            itemlist.insertAdjacentHTML('beforeend', kard.render());
        });
    } catch (err) {
        console.log(`Error: ${err}`);
    }
}

async function Deletethis(itemid) {
    if (confirm("Delete this item?")) {
        const result = await api.deleteItem(itemid);
        if (result.status === 'success') {
            Loadpage();
        } else {
            alert(`Error: ${result.message}`)
        }
    }
}

document.getElementById('add-item-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const name = document.getElementById('item-name').value;
    const qty = document.getElementById('item-qty').value;
    const owner = document.getElementById('item-owner').value;
    const value = document.getElementById('item-value').value;

    const result = api.addItem({
        name: name,
        quantity: qty,
        owner: owner,
        valuation: value
    })

    if (result.status === 'success') {
        document.getElementById('add-item-form').reset();
        Loadpage();
    } else {
        alert(`Error: ${result.message}`)
    }
})