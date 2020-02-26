<template>
  <div id="app" data-app>
    <div id="nav">
      <router-link to="/home"> <button class="btn btn-sm border mx-2">Home</button> </router-link> 
      <router-link to="/cart"><button class="btn btn-sm border mx-2">Cart</button></router-link> 
      <router-link to="/login"><button class="btn btn-sm border mx-2">My Account</button></router-link>
      </div>
    <router-view/>
  </div>
</template>



<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
