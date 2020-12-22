import Vue from 'https://cdn.jsdelivr.net/npm/vue@2.6.11/dist/vue.esm.browser.js'
Vue.component('userform', {
    props: ["addfn"],
    data: function () {
        return {
            user: {name:'', otv:''}
        }
    },
    template: `<div>
                    <input class="form-control" type="text" placeholder="Никнейм" v-model="user.name" />
                    <textarea class="form-control" type="text" placeholder="Отзыв" v-model="user.otv" />
                    <br>
                    <button class="button"  v-on:click="addfn({name:user.name, otv: user.otv})">Добавить</button>
                </div>`
    }
);
Vue.component('useritem', {
    props: ["user", "index", "removefn"],
    template: `<div>
                    <p class="answers">Никнейм: {{user.name}} <br> Отзыв: {{user.otv}}</p>
                    <button class="delete"  v-on:click="removefn(index)">Delete</button>
                </div>`
});
new Vue({
    el: "#app",
    data: {
        users:[]
    },
    methods:{
        remove: function(index){
            this.users.splice(index, 1);
        },
        add: function(user){
            this.users.push(user);
        }
    }
});