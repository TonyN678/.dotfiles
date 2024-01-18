---@diagnostic disable: trailing-space

return {
  
  -- telescope is a fast file-finder
  {
    'nvim-telescope/telescope.nvim', tag = '0.1.5',
    dependencies = { 'nvim-lua/plenary.nvim' },
	  config = function()
      local builtin = require("telescope.builtin")
      
      -- Keybinds
      vim.keymap.set('n', '<leader>ff', builtin.find_files, {})
      vim.keymap.set('n', '<leader>fg', builtin.live_grep, {})
      vim.keymap.set('n', '<leader>fb', builtin.buffers, {})
      vim.keymap.set('n', '<leader>fh', builtin.help_tags, {})
      vim.keymap.set('n', '<leader>fc', builtin.colorscheme, {})
    end
    
  },
  
  -- This plugin provide a telescope-like GUI for other windows involve selecting things
  {
    'nvim-telescope/telescope-ui-select.nvim',
    config = function()
      require("telescope").setup {
      extensions = {
      ["ui-select"] = {
      require("telescope.themes").get_dropdown {}
    }}}
      require("telescope").load_extension("ui-select")
    end
  },
}
