<template>
  <div>
    <!-- ヘッダー~~~~~~ -->
    <header>
      <nav>
        <ul>
          <li><router-link to="#home"><img src="/logo.png" class="logo"></router-link></li>
          <li class="top"><router-link to="#service" class="navigation">SERVICE</router-link></li>
          <li><router-link to="#who" class="navigation">WHO WE ARE</router-link></li>
          <li><router-link to="#about" class="navigation">ABOUT</router-link></li>
          <li><router-link to="#member" class="navigation">MEMBER</router-link></li>
          <li><router-link to="#contact" class="navigation">CONTACT</router-link></li>
        </ul>
      </nav>
    </header>
    <!-- ~~~~~~ヘッダー -->

    <!-- pages読み込み~~~~~~ -->
    <div class="content">
      <nuxt />
    </div>
    <!-- ~~~~~~pages読み込み -->

    <!-- フッター~~~~~~ -->
    <footer>
      <address>
        <p class="center">&copy;Neekey.inc 2019 allright reserved</p>
      </address>
    </footer>
    <!-- ~~~~~~フッター -->
  </div>
</template>

