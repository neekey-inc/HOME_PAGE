<template>
  <section>
    <!-- 決め台詞~~~~~~ -->
    <h1>
      個人の時代に突入する今。<br>
      Neekeyは個人を照らす鍵になる。
    </h1>
    <!-- ~~~~~~決め台詞 -->

    <!-- サービス~~~~~~ -->
    <div class="servicebox">
      <div class="imagebox">
        <img src="/engine.jpg" class="image">
        <p>
          代行エンジン<br>
          代行業を一括で検索・比較・予約できるサイト<br>
          ※2019年10月リリース
        </p>
      </div>
      <div class="imagebox">
        <img src="/homepage.png" class="image">
        <p>
          ホームページ格安開発<br>
          フリーランス・個人事業主、企業様のホームページを<br>
          コミコミ10万円で作成しています。
        </p>
      </div>
      <div class="flexbox">
        <div class="subleftimagebox">
          <img src="/develop.jpg" class="image">
          <p>
            Web、アプリ開発<br>
            受託開発を出来る限りお客様の希望に合う形で開発いたします。<br>
            ※規模により金額が異なるため、お問い合わせください。
          </p>
        </div>
        <div class="subrightimagebox">
          <img src="/seo.jpg" class="image">
          <p>
            SEO対策<br>
            せっかく作ったあなたのサイトが誰にも見られなくては意味ないですよね？<br>
            検索結果上位を獲得するべく力を尽くします。
          </p>
        </div>
      </div>
    </div>
    <!-- ~~~~~~サービス -->

    <!-- アバウト~~~~~~ -->
    <div class="aboutbox">
      <h3 class="about">ABOUT</h3>
      <div class="flexbox">
        <article class="japanese">
          <p>Neekey .Inc</p>
          <p>CEO<br>Takaaki Takada</p>
          <p>Address<br>Dainashiti 1302, 4-41-16 Tyuuou, Nakano-ku, 164-0011 Tokyo, Japan</p>
          <p>Content<br>Internet media and application planning, development, management, SEO measures</p>
          <p>Established<br>2019</p>
        </article>
        <article class="english">
          <p>株式会社ニーキー</p>
          <p>代表者<br>高田 崇照 (たかだ たかあき)</p>
          <p>住所<br>〒164-0011 東京都中野区中央4-41-16ダイナシティ1302</p>
          <p>事業内容<br>インターネットメディア及びアプリケーションの企画・開発・運営、SEO対策</p>
          <p>設立<br>2019年</p>
        </article>
      </div>
    </div>
    <!-- ~~~~~~アバウト -->

    <!-- メンバー~~~~~~ -->
    <div class="memberbox">
      <h3 class="member">MEMBER</h3>
      <div class="flexbox">
        <article class="name">
          <h4>高田 崇照<br>Takaaki Takada</h4>
          <p>得意分野 : 開発、デザイン、経営</p>
          <p>趣味 : お酒とテニス</p>
        </article>
        <article class="description">
          <h4>浅川 実輝<br>Mitsuki Asakawa</h4>
          <p>得意分野 : 開発、財務、人事</p>
          <p>趣味 : 音楽とバスケ</p>
        </article>
      </div>
      <div class="flexbox">
        <article class="name">
          <h4>りょうま<br><br>Ryouma Kamimure</h4>
          <p>得意分野 : 営業、行動、経営</p>
          <p>趣味 : お金と筋トレ</p>
        </article>
        <article class="description">
          <h4>渡邉 和樹<br><br>Kazuki Watanabe</h4>
          <p>得意分野 : SEO対策、Webマーケティング、ブログ</p>
          <p>趣味 : ゲームとサッカー</p>
        </article>
      </div>
    </div>

    <!-- ~~~~~~メンバー -->

    <!-- お問い合わせ~~~~~~ -->
    <div class="contactbox">
      <div class="flexbox">
        <article class="japanese">
          <h3 class="contact">CONTACT</h3>
          <p>
            お仕事のご相談についての質問、お気軽にお問い合わせください<br>
            Having any question about our work? Feel free to ask us.<br>
          </p>
          <p>
            <br>電話でのお問い合わせ先<br>
            You may also call by phone
          </p>
          <p>090-6566-8268<br>(年中無休 10:00~19:00)</p>
        </article>
        <article class="contactform">
          <form id="contact-form" class="col-sm-6 col-md-offset-1 scrollimation fade-left d3" action="contact.php" method="post" novalidate>
            <div class="form-group">
              <label class="control-label" for="contact-name"></label>
              <div class="controls">
                <input id="contact-name" name="contactName" placeholder="　&#xf007; 名前 / Name" class="form-control" type="text" data-error-empty="お名前を入力してください">
              </div>
            </div>
            <div class="form-group">
              <label class="control-label" for="contact-name"></label>
              <div class="controls">
                <input id="contact-company" name="contactCompany" placeholder="　&#xf007; 会社名 / Company Name" class="form-control" type="text">
              </div>
            </div>
            <div class="form-group">
              <label class="control-label" for="contact-mail"></label>
              <div class=" controls">
                <input id="contact-mail" name="email" placeholder="　&#xf0e0; メールアドレス / Email Address" class="form-control" type="email" data-error-empty="メールアドレスを入力してください" data-error-invalid="メールアドレスが正しくありません">
              </div>
            </div>
            <div class="form-group">
              <label class="control-label" for="contact-message"></label>
              <div class="controls">
                <textarea id="contact-message" name="comments" placeholder="　&#xf27a; 内容 / Content" class="form-control" rows="6" type="text" data-error-empty="内容を入力してください"></textarea>
              </div>
            </div>
            <p><button name="submit" type="submit" class="btn btn-color2 btn-block" data-error-message="送信できませんでした" data-sending-message="送信中" data-ok-message="送信しました"><i class="fas fa-paper-plane"></i>　送信する</button></p>
            <input type="hidden" name="submitted" id="submitted" value="true" />
          </form>
        </article>
      </div>
    </div>
    <!-- ~~~~~~お問い合わせ -->
  </section>
</template>

<script>
</script>

<style>
</style>
