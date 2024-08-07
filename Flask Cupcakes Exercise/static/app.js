$(document).ready(function() {
    async function fetchCupcakes() {
        const response = await axios.get('/api/cupcakes');
        const cupcakes = response.data.cupcakes;

        for (let cupcake of cupcakes) {
            $('#cupcakes-list').append(`<li>${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating}</li>`);
        }
    }

    $('#new-cupcake-form').on('submit', async function(evt) {
        evt.preventDefault();
        const flavor = $('input[name="flavor"]').val();
        const size = $('input[name="size"]').val();
        const rating = $('input[name="rating"]').val();
        const image = $('input[name="image"]').val();

        const response = await axios.post('/api/cupcakes', { flavor, size, rating, image });
        const cupcake = response.data.cupcake;

        $('#cupcakes-list').append(`<li>${cupcake.flavor} - ${cupcake.size} - ${cupcake.rating}</li>`);
        this.reset();
    });

    fetchCupcakes();
});