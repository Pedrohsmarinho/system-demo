<template>
    <div class="error-page">
        <section class="error-info">
            <img src="../assets/icons/icone-carro-home.png" alt="" class="img-icon">
            <h1 class="title-error">Dados indisponíveis</h1>
        </section>
    </div>
  </template>
  
  <script>
  export default {
  name: 'ErrorPage',
  created() {
  setTimeout(() => {
    this.$router.push({path: '/'});
  }, 4000);
}

  }
  </script>
  
  <style scoped>
  /*Configurações globais*/
  *{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  /*Configurações da tela inicial*/
  .error-page{
    position: relative;
    height: 100vh;
    width: 100vw;
  
    display: flex;
    justify-content: center;
    background-color: whitesmoke;
  }
  
  
  .error-info{
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  
  .img-icon{
    width: 202px;
    height: 112px;
  }
  
  .title-error{
    color:#9F9F9F;
    font-size:34px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
  
  }
  </style>