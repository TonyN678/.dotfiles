---@diagnostic disable: trailing-space
return {

  -- provide highlights based on installed programming languages
  -- Use :TSInstallInfo to see all parsers
  "nvim-treesitter/nvim-treesitter", 
   build = ":TSUpdate",
   config = function()
   local configs = require("nvim-treesitter.configs")
      configs.setup({
      ensure_installed = {'lua', 'python', 'css', 'html', 'bash'},
      highlight = { enable = true },
      indent = { enable = true }, 
                   })

     vim.keymap.set('n', '<leader>ti', ':TSInstallInfo<CR>', {}) 
  end
}
