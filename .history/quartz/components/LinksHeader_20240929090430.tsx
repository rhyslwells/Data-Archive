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
            <a href="Data-Archive/pages/Data_Archive">Data Archive</a>
          </span>
          <span>
            <a href="Data-Archive/pages/Questions">Questions</a> 
          </span>
          <span>
          <a href="/Data-Archive/Tasks">Tasks</a>
          </span>
        </div>
      <hr style="background-color: var(--gray); border-top: 1px var(--gray) solid; margin-top: 1.3rem"></hr>
      </div>
    )
  }

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor