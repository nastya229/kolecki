document.addEventListener("DOMContentLoaded", function () {
    const productType = document.getElementById("product_type");
    const modelSelect = document.getElementById("model_id");
    const engravingBlock = document.getElementById("engraving-block");
    const viewer = document.getElementById("viewer");

    function updateEngraving() {
        if (!productType || !engravingBlock) return;
        engravingBlock.style.display = productType.value === "ring" ? "block" : "none";
    }

    function filterModels() {
        if (!productType || !modelSelect) return;

        const selectedType = productType.value;

        Array.from(modelSelect.options).forEach((option) => {
            if (!option.value) return;
            const optionType = option.dataset.type;
            option.hidden = optionType !== selectedType;
        });

        modelSelect.value = "";
        if (viewer) {
            viewer.textContent = "Выберите модель для просмотра";
        }
    }

    function updateViewer() {
        if (!modelSelect || !viewer) return;
        const selected = modelSelect.options[modelSelect.selectedIndex];

        if (selected && selected.value) {
            viewer.textContent = `Выбрана модель: ${selected.text}`;
        } else {
            viewer.textContent = "Здесь будет 3D модель";
        }
    }

    if (productType) {
        productType.addEventListener("change", function () {
            updateEngraving();
            filterModels();
        });
    }

    if (modelSelect) {
        modelSelect.addEventListener("change", updateViewer);
    }

    updateEngraving();
    filterModels();
});