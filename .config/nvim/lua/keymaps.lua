-- make shorter map command
-- use keymap.set because it allows set a function in many modes
local Map = vim.keymap.set

local opts = { noremap = true, silent = true }

-- Basic movements between windows (Control + h/j/k/l)
Map({"n", "i"}, "<C-h>", "<C-w>h", opts)
Map({"n", "i"}, "<C-j>", "<C-w>j", opts)
Map({"n", "i"}, "<C-k>", "<C-w>k", opts)
Map({"n", "i"}, "<C-l>", "<C-w>l", opts)

-- resize windows/buffers (Control + Arrow keys)
Map({"n", "i"}, "<C-Up>", ":resize -2<CR>", opts)
Map({"n", "i"}, "<C-Down>", ":resize +2<CR>", opts)
Map({"n", "i"}, "<C-Left>", ":vertical resize -2<CR>", opts)
Map({"n", "i"}, "<C-Right>", ":vertical resize +2<CR>", opts)

-- Using H/L to go to the begining and the end of line
-- Note: H will map to _ (the first non-whitespace character of a line)
-- It would be helpful if it is a indent line in some languages like Python, Ruby, YAML, ...
Map('n', 'H', '_', opts)
Map('n', 'L', '$', opts)

-- Reload configuration without restart nvim
Map('n', '<leader>r', ':source %<CR>')

-- Close all windows and exit from Neovim with <leader> and q
Map('n', '<leader>q', ':qa!<CR>')

-- use U for redo 
Map('n', 'U', '<C-r>', {})

-- Insert empty line without entering insert mode
Map('n', '<leader>o', ':<C-u>call append(line("."), repeat([""], v:count1))<CR>', opts)
Map('n', '<leader>O', ':<C-u>call append(line(".")-1, repeat([""], v:count1))<CR>', opts)

-- Auto go to next or previous error/warning/hint
Map('n', ']]', vim.diagnostic.goto_next) 
Map('n', '[[', vim.diagnostic.goto_prev) 
