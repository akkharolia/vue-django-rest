<template>
    <v-container grid-list-md>
      <v-layout row wrap align-center justify-center fill-height>
        <v-flex md6 offset-3>
       
            <div v-if="!user_login">
            <v-card class="login-card">
                <v-card-title>
                <span class="headline">Register to Amazon</span>
                </v-card-title>

                <v-spacer/>

            </v-card>

            <v-flex md-6 >
                <v-card>
                <v-form ref="register_form" lazy-validation>
                    <v-container>
                        <v-text-field
                        v-model="registration.email"
                        :counter="70"
                        label="Email"
                        maxlength="70"
                        required
                    />

                    <v-text-field
                        type="text"
                        v-model="registration.username"
                        :counter="20"
                        label="Username"
                        maxlength="20"
                        required
                    />

                    <v-text-field
                        type="password"
                        v-model="registration.password1"
                        :counter="20"
                        label="Password"
                        maxlength="20"
                        minlength="8"
                        required
                    />

                    <v-text-field
                        type="password"
                        v-model="registration.password2"
                        :counter="20"
                        label="Confirm Password"
                        maxlength="20"
                        minlength="8"
                        required
                    />

                    </v-container>
                    <button class="btn btn-success px-5 py-2 mb-3" @click="register">Register</button>
                </v-form>
            </v-card>
            </v-flex>
            </div>

            <div v-else>
                <span> YOU ARE LOGGED IN </span>
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
    name: 'Register',
    data: () => ({
        registration:{},
        user_login:false
    }),

    mounted(){
        this.user_login = this.$session.get('user_login')
    },

    methods:{
        register(){
            if (this.$refs.register_form.validate()) {
              axios.post('http://127.0.0.1:8000/rest-auth/registration/', this.registration).then(res => {
                this.$session.start();
                this.$session.set('token', res.data.token);
                this.$session.set('user_login', true);
                swal.fire({icon:'success',text:'Successfully Logged in !!',timer:2000,position:'top-end',showConfirmButton: false,})
                router.push('/login');
              }).catch(error => {
                  console.log(error);
                  swal.fire({icon:'error',title:'Oops...',text:'Something went Wrong !!!'})
                
              })
            }
        }
    }

}
</script>