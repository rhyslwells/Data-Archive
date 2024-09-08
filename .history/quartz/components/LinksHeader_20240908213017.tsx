import { QuartzComponentConstructor } from "./types"
import style from "./styles/linksHeader.scss"

interface Options {
  links: Record<string, string>
}

export default (() => {
  function LinksHeader() {
    return (
      <div>
        <div id="links-header">
          <span>
            <img src="https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Books/Color/books_color.svg"></img>
            <a href="/Sciujo/MAC/MAC">MAC</a>
          </span>
          <span>
            <a href="/Sciujo/Mathematics">Maths</a>
          </span>
        </div>
      <hr style="background-color: var(--gray); border-top: 1px var(--gray) solid; margin-top: 1.3rem"></hr>
      </div>
    )
  }

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor