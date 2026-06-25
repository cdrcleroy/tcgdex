document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("search-form");
    const input = document.getElementById("id_name");
    const res = document.getElementById("autocomplete-results");

    res.style.display = "none";

    let pokemonNames = [];

    const url = '/static/data/card_names_fr.json'

    fetch(url)
        .then(response => response.json())
        .then(json => pokemonNames = json);

    if (input) {
        input.addEventListener("input", () => {
            const query = input.value.trim().toLowerCase();

            if (query.length < 2) {
                res.innerHTML = ""; document.addEventListener("DOMContentLoaded", () => {
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
                            .filter(name => name.toLowerCase().includes(query))
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

                    function handleDocumentClick(event) {
                        const clickInsideResults = resultsBox.contains(event.target);
                        const clickInsideInput = event.target === input;

                        if (!clickInsideResults && !clickInsideInput) {
                            hideSuggestions();
                        }
                    }

                    function handleInputClick() {
                        if (resultsBox.innerHTML !== "") {
                            showSuggestions();
                        }
                    }

                    fetch(DATA_URL)
                        .then(response => response.json())
                        .then(json => {
                            pokemonNames = json;
                        })
                        .catch(error => {
                            console.error("Impossible de charger les noms Pokémon :", error);
                        });

                    hideSuggestions();

                    input.addEventListener("input", handleInput);
                    input.addEventListener("click", handleInputClick);
                    document.addEventListener("click", handleDocumentClick);
                });
                res.style.display = "none";
                return;
            }

            const matches = pokemonNames
                .filter(name => name.toLowerCase().includes(query))
                .slice(0, 8);

            res.innerHTML = "";

            if (matches.length === 0) {
                res.style.display = "none";
                return;
            }

            res.style.display = "flex";

            matches.forEach((match) => {
                const innerDiv = document.createElement("div");
                innerDiv.textContent = match;

                innerDiv.addEventListener("click", () => {
                    input.value = match;
                    res.innerHTML = "";
                    res.style.display = "none";
                    form.requestSubmit();
                });

                res.appendChild(innerDiv);
            });
        });
    };
    document.addEventListener("click", (event) => {
        if (!res.contains(event.target) && event.target !== input) {
            res.style.display = "none";
        }
        if (event.target.id === "id_name" && res.innerHTML != "") {
            res.style.display = "flex";
        }
    });
});
