<template>
    <nav class="reload-info">
        <div class="button-reload">
        <img src="../assets/icons/Mask-group.png" alt="" class="icon-refresh"/>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'ButtomReload'
}
</script>

<style scoped>
/*Configurações globais*/
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.reload-info{
    width: 100%;
    height: 80px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 90px;
}

.button-reload{
    background-color: #6F9AEE;
    width: 250px;
    height: 60px;
    border-radius: 9px;
    display: flex;
    justify-content: center;
    align-items: center;
}
</style>