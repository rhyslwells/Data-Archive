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
            <a href="./pages/Data_Archive">Data Archive</a>
          </span>
          </span>
            <a href="./pages/Questions">Questions</a> 
            </span>
            </span>
            <a href="./Monthly_Review/Goals">Goals</a> 
          </span>
          </span>
          <a href="./Tasks">Tasks</a>
          </span>
        </div>
      <hr style="background-color: var(--gray); border-top: 1px var(--gray) solid; margin-top: 1.3rem"></hr>
      </div>
    )
  }

  LinksHeader.css = style
  return LinksHeader
}) satisfies QuartzComponentConstructor


