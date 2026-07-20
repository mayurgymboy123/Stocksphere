const searchInput = document.getElementById("companySearch");
const searchResults = document.getElementById("searchResults");

searchInput.addEventListener("input", async function () {

    const query = this.value.trim();

    if (query.length < 2) {
        searchResults.classList.add("d-none");
        searchResults.innerHTML = "";
        return;
    }

    const response = await fetch(`/companies/search/?q=${encodeURIComponent(query)}`);
    const data = await response.json();

    if (!data.success) {
        return;
    }

    searchResults.innerHTML = "";

    data.results.forEach(company => {

        searchResults.innerHTML += `
            <div class="search-item" data-symbol="${company.symbol}">
                <strong>${company.instrument_name}</strong><br>
                <span class="search-symbol">${company.symbol}</span>
            </div>
        `;

    });

    document.querySelectorAll(".search-item").forEach(item => {

        item.addEventListener("click", function () {

            const symbol = this.dataset.symbol;

            window.location.href = `/companies/import/${symbol}/`;

        });

    });

    searchResults.classList.remove("d-none");

});