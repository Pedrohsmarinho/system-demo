<template>
    <nav class="search-parking">
        <img src="../assets/icons/Vector.png" alt="" class="icon-search">
        <p class="info-parking">Procurar Estacionamento</p>
        <img src="../assets/icons/expand_more_FILL0_wght400_GRAD0_opsz48.svg" alt="" class="icon-options-parking">
    </nav>
</template>

<script>
export default {
    name: 'SearchInput'
}
</script>

<style scoped>
/*Configurações globais*/
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.search-parking{
    width: 306px;
    height: 41px;
    border-radius: 9px;
    background-color: #F3F3F3;
    display: flex;
    align-items: center;
    flex-direction: row;
    justify-content: space-between;
    align-content: center;
    margin-top: 20px;

}

.info-parking{
    color:#9F9F9F;
    font-size:15px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
}

.icon-search{
    width: 20px;
    margin-left: 7px;
}

.icon-options-parking{
    width: 35px;
}
</style>