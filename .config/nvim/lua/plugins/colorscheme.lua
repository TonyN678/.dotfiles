return {
{
  "folke/tokyonight.nvim",
  lazy = false,
  priority = 1000,

  -- use a function called config will do the same thing as require().setup()
  -- require("tokyonight").setup()
  config = function()
    vim.cmd.colorscheme "tokyonight"

    require("tokyonight").setup({
      style = "storm", -- The theme comes in three styles, `storm`, `moon`, a darker variant `night` and `day`
      light_style = "day", -- The theme is used when the background is set to light
      transparent = false, -- Enable this to disable setting the background color
      sidebars = { "qf", "terminal" },
      })
  end
}
}
