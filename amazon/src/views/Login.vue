<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex md6 offset-3>
                   
            <div v-if="user_login">
                <router-link to="/logout"> <button class="btn btn-info mt-3 px-5 py-2"> LOGOUT </button> </router-link>
            </div>

            <div v-if="!user_login">
            <v-card class="login-card">
                <v-card-title>
                <span class="headline">Login to Amazon</span>
                </v-card-title>

                <v-spacer/>

                <v-card-text>

                <v-layout
                    row
                    fill-height
                    justify-center
                    align-center
                    v-if="loading"
                >
                    <v-progress-circular
                    :size="50"
                    color="primary"
                    indeterminate
                    />
                </v-layout>


                <v-form v-else ref="login_form" lazy-validation>
                    <v-container>

                    <v-text-field
                        v-model="credentials.username"
                        :counter="70"
                        label="username"
                        maxlength="70"
                        required
                    />

                    <v-text-field
                        type="password"
                        v-model="credentials.password"
                        :counter="20"
                        label="password"
                        maxlength="20"
                        required
                    />

                    </v-container>
                    <button class="btn btn-success px-5 py-2" @click="login">Login</button>

                </v-form>

                <router-link to="/register"> <button class="btn btn-info mt-3 px-5 py-2"> Register </button> </router-link>
                
                </v-card-text>
            </v-card>
            </div>

        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import router from '../router';
import axios from 'axios';
import swal from 'sweetalert2';

export default {
    name: 'Login',
    data: () => ({
        credentials: {},
        registration:{},
        loading: false,
        user_login:false,
        dialog: false,

    }),

    mounted(){
        this.user_login = this.$session.get('user_login')
    },

    methods:{
        login() {
          // checking if the input is valid
            if (this.$refs.login_form.validate()) {
              this.loading = true;
              axios.post('http://localhost:8000/api/auth/obtain_token/', this.credentials).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                this.$session.set('user_login', true);
                swal.fire({icon:'success',text:'Successfully Logged in !!',timer:2000,position:'top-end',showConfirmButton: false,})
                router.push('/home');
              }).catch(error => {
                  this.loading = false;
                  console.log(error);
                  swal.fire({icon:'error',title:'Oops...',text:'Something went Wrong !!!'})
                
              })
            }
        },
        logout(){
            this.$session.remove('token')
            this.$session.remove('user_login')
            this.dialog = false
            // this.$session.set('user_login',false)
            swal.fire({icon:'success',text:'You Have been Logged Out !',timer:2000,position:'top-end',showConfirmButton: false,})
            router.push('/login')
        }
    }

}
</script>