---@diagnostic disable: trailing-space
return {
  'akinsho/bufferline.nvim',
  version = "*",
  dependencies = {'nvim-tree/nvim-web-devicons'},
  config = function()
    require("bufferline").setup{
      options = {
      separator_style = "slant",
      enforce_regular_tabs = true,
      always_show_bufferline = false,
      hover = { enabled = true, delay = 200, reveal = {'close'}},
      color_icons = true,      
      show_buffer_icons = true, -- disable filetype icons for buffers
      show_buffer_close_icons = true,
      show_close_icon = true,
      show_tab_indicators = true,
      
        offsets = {
        {
            filetype = "NvimTree",
            text = "File Explorer",
            highlight = "Directory",
            separator = true -- use a "true" to enable the default, or set your own character
        }
    },

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

      highlights = {
        fill = {
         --       fg = '<colour-value-here>',
                bg = '#282A36',
            },
            background = {
                fg = '#ffffff',
                bg = '#282A36',
            },

    }
    } 
    -- Keybindings
    vim.keymap.set({'n', }, '<C-]>', ':BufferLineCycleNext<CR>', {})
    vim.keymap.set({'n', }, '<C-[>', ':BufferLineCyclePrev<CR>', {})
    vim.keymap.set({'n', 'i'}, '<C-p>', ':BufferLineTogglePin<CR>', {})
    vim.keymap.set({'n'}, '<leader>P', ':BufferLinePick<CR>', {})
    --vim.keymap.set({'n'}, '<leader>bc', ':BufferLinePickClose', {})
    vim.keymap.set({'n'}, '<leader>bc', ':close<CR>', {})

  end
}
