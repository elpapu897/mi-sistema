const AMAZON_IMAGE =
  "https://images.unsplash.com/photo-1594675610313-f427344ac988?auto=format&fit=crop&q=88&w=2400";

const chapters = [
  {
    number: "01",
    title: "Agua",
    text: "Un pulso de ríos, lluvias y bosques inundables que conecta los Andes con el Atlántico.",
    className: "chapter-water",
  },
  {
    number: "02",
    title: "Bosque",
    text: "Millones de hectáreas de vida entrelazada: cada estrato sostiene al siguiente.",
    className: "chapter-forest",
  },
  {
    number: "03",
    title: "Memoria",
    text: "Más de 420 pueblos indígenas mantienen lenguas, saberes y formas de cuidar el territorio.",
    className: "chapter-memory",
  },
];

export default function Home() {
  return (
    <main id="contenido">
      <a className="skip-link" href="#territorio">Saltar al contenido</a>
      <header className="site-header">
        <a className="brand" href="#inicio" aria-label="Amazonía Viva, ir al inicio">
          <span className="brand-mark" aria-hidden="true" />
          AMAZONÍA VIVA
        </a>

        <nav className="desktop-nav" aria-label="Navegación principal">
          <a href="#territorio">Territorio</a>
          <a href="#voces">Voces</a>
          <a href="#cuidar">Cómo cuidar</a>
        </nav>

        <details className="mobile-menu">
          <summary aria-label="Abrir menú"><span>MENÚ</span></summary>
          <nav aria-label="Navegación móvil">
            <a href="#territorio">Territorio</a>
            <a href="#voces">Voces</a>
            <a href="#cuidar">Cómo cuidar</a>
          </nav>
        </details>
      </header>

      <section className="hero" id="inicio" aria-labelledby="hero-title">
        <div className="hero-photo" style={{ backgroundImage: `url(${AMAZON_IMAGE})` }}>
          <div className="hero-shade" />
        </div>
        <div className="hero-orbit orbit-one" aria-hidden="true" />
        <div className="hero-orbit orbit-two" aria-hidden="true" />

        <div className="hero-content">
          <p className="eyebrow light"><span /> Un territorio que respira</p>
          <h1 id="hero-title">
            DONDE LA<br />
            <em>VIDA</em> NO<br />
            TERMINA
          </h1>
          <div className="hero-bottom">
            <p>
              La Amazonía no es un paisaje lejano.<br />
              Es agua, cultura y futuro en movimiento.
            </p>
            <a className="round-link" href="#territorio" aria-label="Descubrir el territorio">
              <span>DESCUBRIR</span>
              <b aria-hidden="true">↓</b>
            </a>
          </div>
        </div>

        <p className="hero-caption">CUENCA AMAZÓNICA · SUDAMÉRICA</p>
      </section>

      <div className="fact-ribbon" aria-label="Datos destacados">
        <div>
          <span>6,7 MILLONES KM²</span><i>•</i>
          <span>10% DE LAS ESPECIES CONOCIDAS</span><i>•</i>
          <span>MÁS DE 420 PUEBLOS INDÍGENAS</span><i>•</i>
          <span aria-hidden="true">6,7 MILLONES KM²</span><i aria-hidden="true">•</i>
          <span aria-hidden="true">10% DE LAS ESPECIES CONOCIDAS</span>
        </div>
      </div>

      <section className="manifesto" id="territorio">
        <div className="section-index">
          <span>01</span>
          <span>EL TERRITORIO</span>
        </div>
        <div className="manifesto-copy">
          <p className="eyebrow"><span /> Mucho más que una selva</p>
          <h2>
            NO ES EL PULMÓN<br />
            DEL MUNDO.<br />
            <em>ES SU LATIDO.</em>
          </h2>
          <div className="manifesto-note">
            <p>
              La Amazonía es el bosque tropical más extenso del planeta: una red viva que regula lluvias,
              mueve agua dulce y alberga una diversidad imposible de separar de quienes la habitan.
            </p>
            <a href="#capitulos">Explorar sus dimensiones <span aria-hidden="true">↘</span></a>
          </div>
        </div>
      </section>

      <section className="chapters" id="capitulos" aria-label="Dimensiones de la Amazonía">
        {chapters.map((chapter) => (
          <article className={`chapter ${chapter.className}`} key={chapter.number}>
            <span className="chapter-number">{chapter.number}</span>
            <div className="chapter-content">
              <h3>{chapter.title}</h3>
              <p>{chapter.text}</p>
            </div>
            <span className="chapter-arrow" aria-hidden="true">↗</span>
          </article>
        ))}
      </section>

      <section className="numbers" aria-labelledby="numbers-title">
        <div className="numbers-heading">
          <p className="eyebrow light"><span /> Una escala difícil de imaginar</p>
          <h2 id="numbers-title">UN MUNDO<br />DENTRO DEL<br /><em>MUNDO</em></h2>
        </div>
        <div className="stats-grid">
          <article>
            <strong>6,7</strong>
            <span>millones de km² de bioma amazónico</span>
          </article>
          <article>
            <strong>10%</strong>
            <span>de las especies conocidas del planeta</span>
          </article>
          <article>
            <strong>420+</strong>
            <span>pueblos indígenas en la región</span>
          </article>
          <article>
            <strong>40M</strong>
            <span>de personas llaman hogar a la Amazonía</span>
          </article>
        </div>
        <p className="numbers-source">Fuentes: WWF y Organización del Tratado de Cooperación Amazónica.</p>
      </section>

      <section className="voices" id="voces">
        <div className="voices-image">
          <div className="image-frame" style={{ backgroundImage: `url(${AMAZON_IMAGE})` }} role="img" aria-label="Río serpenteando a través del bosque amazónico" />
          <span className="vertical-label">TERRITORIO VIVO · 03°S</span>
        </div>
        <div className="voices-copy">
          <div className="section-index dark">
            <span>02</span>
            <span>QUIENES LA CUIDAN</span>
          </div>
          <blockquote>
            “PROTEGER LA AMAZONÍA EMPIEZA POR ESCUCHAR A QUIENES LA CONOCEN DESDE SIEMPRE.”
          </blockquote>
          <p>
            Los pueblos indígenas y las comunidades locales son guardianes de bosques ricos en carbono,
            biodiversidad y memoria. Defender sus derechos territoriales es también defender el equilibrio del planeta.
          </p>
          <a href="https://otca.org/en/eixo/indigenous-peoples/" target="_blank" rel="noreferrer">
            Conocer su papel <span aria-hidden="true">↗</span>
          </a>
        </div>
      </section>

      <section className="action" id="cuidar">
        <p className="eyebrow"><span /> La selva no necesita espectadores</p>
        <div className="action-layout">
          <h2>HACER LUGAR<br />AL <em>FUTURO.</em></h2>
          <div className="action-copy">
            <p>
              Informarse también es una forma de cuidar. Conocé el territorio, amplificá las voces locales y elegí
              iniciativas que pongan la vida por delante de la extracción.
            </p>
            <div className="action-links">
              <a href="https://wwf.panda.org/discover/knowledge_hub/where_we_work/amazon/about_the_amazon" target="_blank" rel="noreferrer">
                Explorar datos del bioma <span aria-hidden="true">↗</span>
              </a>
              <a href="https://science.nasa.gov/earth/earth-observatory/indigenous-communities-protect-the-amazon-151921/" target="_blank" rel="noreferrer">
                Ver la Amazonía desde el espacio <span aria-hidden="true">↗</span>
              </a>
            </div>
          </div>
        </div>
      </section>

      <footer>
        <a className="brand footer-brand" href="#inicio">
          <span className="brand-mark" aria-hidden="true" />
          AMAZONÍA VIVA
        </a>
        <p>Una historia original para mirar el territorio de cerca.</p>
        <div className="footer-meta">
          <span>AMAZONÍA · 2026</span>
          <a href="#inicio">VOLVER ARRIBA ↑</a>
        </div>
      </footer>
    </main>
  );
}
