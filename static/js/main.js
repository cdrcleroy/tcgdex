document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("search-form");
    const input = document.getElementById("id_name");
    const resultsBox = document.getElementById("autocomplete-results");

    if (!form || !input || !resultsBox) {
        return;
    }

    const DATA_URL = "/static/data/card_names_fr.json";
    const MIN_QUERY_LENGTH = 2;
    const MAX_RESULTS = 8;

    let pokemonNames = [];

    function showSuggestions() {
        resultsBox.style.display = "flex";
    }

    function hideSuggestions() {
        resultsBox.style.display = "none";
    }

    function clearSuggestions() {
        resultsBox.innerHTML = "";
        hideSuggestions();
    }

    function getMatches(query) {
        return pokemonNames
            .filter((name) => name.toLowerCase().includes(query))
            .slice(0, MAX_RESULTS);
    }

    function selectSuggestion(name) {
        input.value = name;
        clearSuggestions();
        form.requestSubmit();
    }

    function renderSuggestions(matches) {
        resultsBox.innerHTML = "";

        if (matches.length === 0) {
            hideSuggestions();
            return;
        }

        matches.forEach((match) => {
            const item = document.createElement("div");
            item.classList.add("autocomplete-item");
            item.textContent = match;

            item.addEventListener("click", () => {
                selectSuggestion(match);
            });

            resultsBox.appendChild(item);
        });

        showSuggestions();
    }

    function handleInput() {
        const query = input.value.trim().toLowerCase();

        if (query.length < MIN_QUERY_LENGTH) {
            clearSuggestions();
            return;
        }

        const matches = getMatches(query);
        renderSuggestions(matches);
    }

    function handleInputClick() {
        if (resultsBox.innerHTML !== "") {
            showSuggestions();
        }
    }

    function handleDocumentClick(event) {
        const clickInsideResults = resultsBox.contains(event.target);
        const clickInsideInput = event.target === input;

        if (!clickInsideResults && !clickInsideInput) {
            hideSuggestions();
        }
    }

    fetch(DATA_URL)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`HTTP ${response.status}`);
            }

            return response.json();
        })
        .then((json) => {
            pokemonNames = json;
        })
        .catch((error) => {
            console.error(
                "Impossible de charger les noms Pokémon :",
                error
            );
        });

    hideSuggestions();

    input.addEventListener("input", handleInput);
    input.addEventListener("click", handleInputClick);
    document.addEventListener("click", handleDocumentClick);
});
