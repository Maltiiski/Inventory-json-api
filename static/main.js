class APIClient {
    constructor(baseURL = '/api') {
        this.baseURL = baseURL;
    }

    async deleteItem(itemId) {
        const response = await fetch(`${this.baseURL}/items/${itemId}`, {method: 'DELETE'});
        return await response.json();
    }

    async fetchAllItems() {
        const response = await fetch(`${this.baseURL}/items`);
        return await response.json();
    }

    async addItem(itemData) {
        const response = await fetch(`${this.baseURL}/inventory`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(itemData)
        });
        return await response.json();
    }
}