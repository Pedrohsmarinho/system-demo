<template>
    <div id="dashboard">
        <SearchInput/>
        <div class="dashboard-number">
            <p class="dashboard-number-texts">TOTAL DE VAGAS</p>
            <div class="vacancies">
                <div class="vacancies-number">
                    <div class="vacancies-dashboard" style="background-color: #198F6C;">{{situacaoDoEstacionamento.data.vagaslivres}}</div>
                    <p class="dashboard-number-texts">Livres</p>
                </div>
                <div class="vacancies-number">
                    <div class="vacancies-dashboard" style="background-color: #E90B0B;">{{situacaoDoEstacionamento.data.vagasOcupadas}}</div>
                    <p class="dashboard-number-texts">Ocupadas</p>
                </div>
            </div>
        </div>
        <div class="text-info">
            <small>Data: {{situacaoDoEstacionamento.data.dataDeAtualizacao}}</small><br/>
            <small>Última Atualização: {{situacaoDoEstacionamento.data.horaDeAtualizacao}}</small><br/>
            <small>Local: {{situacaoDoEstacionamento.data.localDoEstacionamento}}</small>
        </div>
        <ButtomReload/>
    </div>
    
</template>

<script>
import ButtomReload from '../components/ButtomReload.vue'
import SearchInput from '../components/SearchInput.vue'
import {api} from '../services.js'

export default {
    name: 'HomePage',
  components: {
    ButtomReload,
    SearchInput,
  },
  data(){
    return{
    situacaoDoEstacionamento: null,
    }},
    methods:{
        getVagas(){
            api.get('/dadosSobreVagas')
            .then(response => {
                console.log("response da api");
                console.log(response.data);
                this.situacaoDoEstacionamento = response
            })

             if(this.situacaoDoEstacionamento == null){
                    this.$router.push({path: '/errorpage'});
            } 
        }
    },
    created(){
        this.getVagas()
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

#dashboard{
    margin: 0;
    padding: 0;
    position: relative;
    height: 100vh;
    width: 100vw;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-direction: column;
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

.dashboard-number{
    width: 100%;
    height: 250px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    justify-content: space-around;
    margin-top: 20px;
}

.text-info{
    width: 100%;
    height: 80px;
    padding: 10px;
    margin-bottom: 30px;
}

small{
    color:#9F9F9F;
    font-size:15px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
    margin-left: 5px;
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

.vacancies{
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: row;
}

.vacancies-number{
    width: 100%;
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
}

.vacancies-dashboard{
    width: 150px;
    height: 145px;
    background-color: red;
    border-radius: 9px;
    color:white;
    font-size:59px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
    display: flex;
    justify-content: center;
    align-items: center;
}

.dashboard-number-texts{
    color:#9F9F9F;
    font-size:20px;
    font-style: Bold;
    font-family: 'Secular One', sans-serif;
}
</style>