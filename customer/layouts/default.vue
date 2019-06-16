<template>
  <div>
    <header>
      <el-input placeholder="例) 家事代行"></el-input><a @click="$router.push({name:'category'})"><el-button icon="el-icon-search"></el-button></a>
      <el-button><a @click="$router.push({name:'home'})">ロゴ</a></el-button>
      <a @click="$router.push({name:'user-sign'})"><i class="el-icon-user-solid"></i></a>
      <el-dropdown>
        <i class="el-icon-arrow-down el-icon-menu"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item><a @click="$router.push({name:'about'})">代行ENGINEとは？</a></el-dropdown-item>
          <el-dropdown-item><a @click="$router.push({name:'about'})">運営会社：Neekey.inc</a></el-dropdown-item>
          <el-dropdown-item><a @click="$router.push({name:'question'})">よくある質問</a></el-dropdown-item>
          <el-dropdown-item><a @click="$router.push({name:'contact'})">お問い合わせ</a></el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </header>
    <div class="content">
      <nuxt />
    </div>
    <footer>
      <div>
        <h3>代行一覧</h3>
        <a></a>
      </div>
      <div>
        <h3>代行ENGINEについて</h3>
        <a @click="$router.push({name:'about'})">代行ENGINEとは？</a>
        <a @click="$router.push({name:'about'})">運営会社：Neekey.inc</a>
        <a @click="$router.push({name:'question'})">よくある質問</a>
        <a @click="$router.push({name:'contact'})">お問い合わせ</a>
        <a @click="$router.push({name:'privacy'})">プライバシーポリシー</a>
        <a @click="$router.push({name:'terms'})">利用規約</a>
      </div>
      <div>
        <h3>店舗・法人様向け</h3>
        <a @click="$router.push({name:'advertise'})">掲載したい企業様はこちら</a>
        <a @click="$router.push({name:'published'})">広告を載せたい企業様はこちら</a>
      </div>
      <address>&copy;Neekey.inc 2019 allright reserved 無断転載禁止</address>
    </footer>
  </div>
</template>
