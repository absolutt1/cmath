import { createClient } from '@supabase/supabase-js'

if (!process.env.NEXT_PUBLIC_SUPABASE_URL || !process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY) {
  throw new Error('Missing Supabase environment variables')
}

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
)

export async function insertDocument(content, url) {
  const { data, error } = await supabase
    .from('documents')
    .insert([
      {
        content: content,
        url: url
      }
    ])
    .select()

  if (error) throw error
  return data[0]
}