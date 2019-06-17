<template>
  <div>
    <!-- ヘッダー~~~~~~ -->
    <header>
      <nav>
        <ul>
          <li><img src="/key.png" class="logo"></li>
          <li>COMPANY</li>
          <li>SERVICE</li>
          <li>ABOUT</li>
          <li>MEMBER</li>
          <li>CONTACT</li>
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
