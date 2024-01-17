return {
  {'akinsho/toggleterm.nvim',
    version = "*",
    config = function()
      require("toggleterm").setup{

        -- use Ctrl+\ to open terminal  
        -- To open a 2nd terminal, exit to normal mode by Esc, then type 2<C-\>
        open_mapping = [[<C-\>]],
        shade_terminals = true,
        shading_factor = 2,
        shade_filetypes = {},
        start_in_insert = true,
        insert_mappings = true, -- whether or not the open mapping applies in insert mode
        persist_size = true,
        size = function(term)
           if term.direction == "horizontal" then
             return 10 
           elseif term.direction == "vertical" then
             return 30
           end
        end,
        close_on_exit = true,
        shell = vim.o.shell,
        -- Options for direction: 'vertical' | 'horizontal' | 'tab' | 'float'
        direction = "horizontal",

        float_opts = {
    -- The border key is *almost* the same as 'nvim_open_win'
    -- see :h nvim_open_win for details on borders however
    -- the 'curved' border is a custom border type
    -- not natively supported but implemented in this plugin.
    -- 'single' | 'double' | 'shadow' | 'curved' |   
         border = "curved",
         width = 1000,
         height = 500,
         winblend = 3,
         zindex = 100,
       },
      }

      function _G.set_terminal_keymaps()
         local opts = {noremap = true}
         vim.keymap.set('t', '<esc>', [[<C-\><C-n>]], opts)
         --vim.keymap.set('t', 'jk', [[<C-\><C-n>]], opts)
         vim.keymap.set('t', '<C-h>', [[<Cmd>wincmd h<CR>]], opts)
         vim.keymap.set('t', '<C-j>', [[<Cmd>wincmd j<CR>]], opts)
         vim.keymap.set('t', '<C-k>', [[<Cmd>wincmd k<CR>]], opts)
         vim.keymap.set('t', '<C-l>', [[<Cmd>wincmd l<CR>]], opts)
         vim.keymap.set('t', '<C-w>', [[<C-\><C-n><C-w>]], opts)
      end

-- if you only want these mappings for toggle term use term://*toggleterm#* instead
vim.cmd('autocmd! TermOpen term://* lua set_terminal_keymaps()')
    end
  }
}
