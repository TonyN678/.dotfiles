---@diagnostic disable: trailing-space
return {
  'akinsho/bufferline.nvim',
  version = "*",
  dependencies = {'nvim-tree/nvim-web-devicons'},
  config = function()
    require("bufferline").setup{
      options = {
      separator_style = "slope",
      enforce_regular_tabs = true,
      always_show_bufferline = false,
      hover = { enabled = true, delay = 200, reveal = {'close'}},
      offsets = {
        {
          filetype = "NvimTree",
          text = "File Explorer",
          text_align = "center",
          separator = true,
        }
      },
      color_icons = true,      
      show_buffer_icons = true, -- disable filetype icons for buffers
      show_buffer_close_icons = true,
      show_close_icon = true,
      show_tab_indicators = true,
      
            indicator = {
                icon = '▎', -- this should be omitted if indicator style is not 'icon'
                style =  'underline',
            },
            buffer_close_icon = '󰅖',
            modified_icon = '●',
            close_icon = '',
            left_trunc_marker = '',
            right_trunc_marker = '',
        groups = {
            items = {
                require('bufferline.groups').builtin.pinned:with({ icon = "" })
            }
        }

      },
    }
    
    -- Keybindings
    vim.keymap.set({'n', 'i'}, '<C-]>', ':BufferLineCycleNext<CR>', {})
    vim.keymap.set({'n', 'i'}, '<C-[>', ':BufferLineCyclePrev<CR>', {})
    vim.keymap.set({'n', 'i'}, '<C-p>', ':BufferLineTogglePin<CR>', {})
    vim.keymap.set({'n'}, '<leader>P', ':BufferLinePick<CR>', {})
    --vim.keymap.set({'n'}, '<leader>bc', ':BufferLinePickClose', {})
    vim.keymap.set({'n'}, '<leader>bc', ':close<CR>', {})

  end
}
