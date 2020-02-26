<template v-if="user_login">
    <v-row justify="center">
        <v-col md4 offset-1>
            <v-dialog v-model="dialog" persistent max-width="290">
        <template v-slot:activator="{ on }" class="ml-5">
            <v-btn color="primary px-5 py-1 ml-5"  dark v-on="on">Logout</v-btn>
        </template>
        <v-card>
            <v-card-title class="headline">Logout   </v-card-title>
            <v-card-text>Are You Sure you want to logout ?</v-card-text>
            <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" text @click="dialog = false">No</v-btn>
            <v-btn color="green darken-1" text @click="logout()" >Yes</v-btn>
            </v-card-actions>
        </v-card>
        </v-dialog>
        </v-col>
    </v-row>
    </template>

<script>
import router from '../router';
import swal from 'sweetalert2';

export default {
    name:'Logout',
    data(){
        return {
            dialog:false
        }
    },
    methods:{
        logout(){
            this.$session.remove('token')
            this.$session.remove('user_login')
            router.push('/login')
            // this.$session.set('user_login',false)
            swal.fire({icon:'success',text:'You Have been Logged Out !',timer:2000,position:'top-end',showConfirmButton: false,})
            
        }
    }
}
</script>